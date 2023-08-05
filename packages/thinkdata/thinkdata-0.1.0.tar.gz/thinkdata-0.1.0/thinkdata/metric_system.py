import re
import math
from typing import List
import pandas as pd


class MetricSystem():
    """
    基于指标体系的分析工具类
    """

    def __init__(self, relations) -> None:
        self.relation_map = MetricSystem._parse_relations(relations)

    # 下面是一些的基本的方法

    @staticmethod
    def _parse_relations(relations):
        """
        解析指标之间的关系表达式，支持单一的+-*/，不支持关系式中出现多个不同的关系符
        """
        relation_map = {}
        for relation in relations:
            if re.search(r"\=", relation):
                relation_info = MetricSystem._parse_equation(relation)
                new_map = {
                    relation_info["parent"]: {
                        "relation": relation_info["relation"],
                        "childs": relation_info["childs"]
                    }
                }
                for child in relation_info["childs"]:
                    if child not in relation_map:
                        relation_map.update({child: None})
            else:
                new_map = {
                    relation: None
                }
            relation_map.update(new_map)
        return relation_map

    @ staticmethod
    def _parse_equation(equation):
        """
        解析等式
        """
        left, right = re.split(r"\s*\=\s*", equation.strip())
        relation = re.search(r"([\+\-\*\/])", right).group()
        childs = re.split(r"\s*[\+\-\*\/]\s*", right.strip())
        result = {
            "parent": left,
            "relation": relation,
            "childs": childs
        }
        return result

    def get_childs(self, metric) -> List[str]:
        """
        获取子指标
        """
        if metric in self.relation_map:
            node = self.relation_map.get(metric)
            if node is None:
                return None
            else:
                return node.get("childs")
        else:
            raise KeyError(f"{metric}")

    def get_relation(self, metric) -> str:
        """
        获取子指标的关系
        """
        if metric in self.relation_map:
            node = self.relation_map.get(metric)
            if node is None:
                return None
            else:
                return node.get("relation")
        else:
            raise KeyError(f"{metric}")

    def check_data(self, df, threshold=0.02):
        """
        检查数据集是否符合指标体系的定义

        threshold:
            设置数据差异的阈值，阈值越小，要求差异越小
        """
        for metric in self.relation_map:
            check_data = self.get_check_data(
                df, metric=metric, threshold=threshold)
            if check_data is not None and not check_data["_check"].all():
                raise ValueError(f'"{metric}"的实际数据关系与指标体系不一致')
        return True

    def get_check_data(self, df, metric, threshold=0.02):
        """
        获取数据集检查的数据集
        """
        node = self.relation_map[metric]
        if node is not None:
            relation = node["relation"]
            child_columns = node["childs"]
            columns = [metric] + child_columns
            sdf = df[columns]
            sdf = sdf.assign(
                _stat=sdf.apply(
                    lambda x: MetricSystem._get_stat(
                        x[1:], relation=relation),
                    raw=True,
                    axis=1),
            )
            # 检查单行数据是否符合指标体系的定义
            sdf = sdf.assign(
                _check=sdf[[metric, "_stat"]].apply(
                    lambda x: abs(1 - x[0]/x[1]) <= threshold, axis=1, raw=True)
            )
            return sdf
        else:
            return None

    @staticmethod
    def _get_stat(child_values, relation):
        stat = 0
        if relation == "+":
            stat = sum(child_values)
        elif relation == "-":
            stat = (child_values[0] - sum(child_values[1:]))
        elif relation in ("*", "/"):
            stat = child_values[0]
            for x in child_values[1:]:
                if relation == "*":
                    stat *= x
                else:
                    stat /= x
        return stat

    # 开始指标层级表的部分

    def build_hierarchy_table(self, df: pd.DataFrame, metric: str, max_depth: int = None):
        """
        基于原来的指标数据表，构建指定指标的指标层级表，便于后续分析或可视化

        例子

        >> df = pd.DataFrame([[1,2,3]],columns=list("abc"))
        >> ms = MetricSystem(relations=["c = a + b"])
        >> print(ms.build_hierarchy_table(df,metric="c"))

          lv1 lv2  value
        0   c   a      1
        0   c   b      2

        """
        paths = self._search_leaf_paths(metric, filter_relation="+")
        max_depth_actual = max([len(x) for x in paths])

        standard_depth = min(max_depth_actual, max_depth) if isinstance(
            max_depth, int) else max_depth_actual

        records = []
        keys = []
        for path in paths:
            leaf_metric = path[-1]
            dims = MetricSystem._fix_path(path, standard_depth)
            for key, value in df[leaf_metric].items():
                record = dims + [value]
                records.append(record)
                keys.append(key)
        columns = [f"lv{i}" for i in range(
            1, standard_depth + 1)] + ["value"]
        table = pd.DataFrame(records, columns=columns, index=keys)
        return table

    @staticmethod
    def _fix_path(path: List, depth: int):
        """
        根据需要的长度调整层次路径的长短
        """
        n = len(path)
        if n >= depth:
            return path[:depth]
        else:
            return path + [None] * (depth - n)

    def _search_leaf_paths(self, metric, filter_relation=None):
        """
        搜索目标指标的所有抵达叶节点的层次路径
        """
        paths = []
        base_path = [metric]
        childs = self.get_childs(metric)
        if filter_relation is not None:
            relation = self.get_relation(metric)
            if relation != filter_relation:
                path = base_path
                paths.append(path)
                return paths
        if childs is not None:
            for child in childs:
                child_paths = self._search_leaf_paths(
                    child, filter_relation=filter_relation)
                for child_path in child_paths:
                    path = base_path + child_path
                    paths.append(path)
        else:
            path = base_path
            paths.append(path)
        return paths

    # 开始差异原因分析的部分

    @staticmethod
    def calc_influence(source_from, source_to, target_from, target_to, relation, location_index) -> float:
        """
        计算影响度
        """
        if relation in ("+", "-"):
            influence = (source_to - source_from)/(target_to - target_from)
            if relation == "-" and location_index == 1:
                influence = -1 * influence
        elif relation in ["*", "/"]:
            influence = math.log(source_to/source_from) / \
                math.log(target_to/target_from)
            if relation == "/" and location_index == 1:
                influence = -1 * influence
        return round(influence, 2)

    def analyze_diff(self, df, idx_list, metric) -> pd.DataFrame:
        """
        分析不同数据记录之间指标差异的原因，以数据集形式返回
        """
        records = self._get_analyze_diff_records(df, idx_list, metric, level=1)
        result_df = pd.DataFrame(records).sort_values(by=["level", "influence"],
                                                      ascending=[True, False]).reset_index(drop=True)
        return result_df

    def _get_analyze_diff_records(self, df, idx_list, metric, level=1):
        """
        分析不同数据记录之间指标差异的原因

        idx_list: 
            记录的索引号列表，目前只支持两条记录之间进行对比，例如[1,2]
        """
        left, right = idx_list

        records = []
        if metric in self.relation_map:
            node = self.relation_map.get(metric)
            if node is not None:
                relation = node["relation"]
                for location_index, child in enumerate(node["childs"]):
                    source_from = df.loc[left, child]
                    source_to = df.loc[right, child]
                    target_from = df.loc[left, metric]
                    target_to = df.loc[right, metric]
                    influence = MetricSystem.calc_influence(
                        source_from, source_to, target_from, target_to, relation, location_index)
                    record = {
                        "source": child,
                        "source_from": source_from,
                        "source_to": source_to,
                        "target": metric,
                        "target_from": target_from,
                        "target_to": target_to,
                        "relation": relation,
                        "level": level,
                        "influence": influence, }
                    records.append(record)
                    if child in self.relation_map:
                        child_records = self._get_analyze_diff_records(
                            df, idx_list=idx_list, metric=child, level=level+1)
                        records.extend(child_records)
        return records
