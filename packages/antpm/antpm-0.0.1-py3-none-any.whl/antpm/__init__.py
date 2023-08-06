# encoding=UTF-8

import re

glob_pattern = r"\?|\*"


# noinspection PyMethodMayBeStatic
class AntPathMatcher(object):
    def __int__(self):

        pass

    def match(self, pattern: str, path: str) -> bool:
        patt_dirs: list[str] = [item for item in pattern.split("/") if item is not None and len(item) > 0]
        path_dirs: list[str] = [item for item in path.split("/") if item is not None and len(item) > 0]

        patt_idx_start = 0
        patt_idx_end = len(patt_dirs) - 1
        path_idx_start = 0
        path_idx_end = len(path_dirs) - 1

        # 类似 /test.jpg test.jpg
        if path is None or path.startswith("/") != pattern.startswith("/"):
            return False

        while patt_idx_start <= patt_idx_end and path_idx_start <= path_idx_end:
            patt_dir = patt_dirs[patt_idx_start]
            if patt_dir == "**":
                break
            if not self.__match_str(patt_dir, path_dirs[patt_idx_start]):
                return False
            path_idx_start += 1
            patt_idx_start += 1

        # 字符串已经匹配走完了，但是pattern还没有走完
        if path_idx_start > path_idx_end:
            if patt_idx_start > patt_idx_end:
                return pattern.endswith("/") == path.endswith("/")
            if patt_idx_start == patt_idx_end and patt_dirs[patt_idx_start] == "*" and path.endswith("/"):
                return True
            for i in range(patt_idx_start, patt_idx_end + 1):
                if patt_dirs[i] != "**":
                    return False
            return True
        elif patt_idx_start > patt_idx_end:
            return False

        while patt_idx_start <= patt_idx_end and path_idx_start <= path_idx_end:
            patt_dir = patt_dirs[patt_idx_end]
            if patt_dir == "**":
                break
            if not self.__match_str(patt_dir, path_dirs[path_idx_end]):
                return False
            if patt_idx_end == len(patt_dirs) - 1 and pattern.endswith("/") != path.endswith("/"):
                return False
            patt_idx_end -= 1
            path_idx_end -= 1

        if path_idx_start > path_idx_end:
            for i in range(patt_idx_start, patt_idx_end + 1):
                if patt_dirs[i] != "**":
                    return False
            return True

        while patt_idx_start != patt_idx_end and path_idx_start <= path_idx_end:
            patt_idx_tmp = -1
            for i in range(patt_idx_start + 1, patt_idx_end + 1):
                if patt_dirs[i] == "**":
                    patt_idx_tmp = i
                    break
            if patt_idx_tmp == patt_idx_start + 1:
                patt_idx_start += 1
                continue

            pat_len = patt_idx_tmp - patt_idx_start - 1
            path_len = path_idx_end - path_idx_start + 1
            found_idx = -1

            for i in range(path_len - pat_len + 1):
                continue_flag = True
                for j in range(pat_len):
                    sub_pat = patt_dirs[patt_idx_start + j + 1]
                    sub_str = path_dirs[path_idx_start + i + j]
                    if not self.__match_str(sub_pat, sub_str):
                        continue_flag = False
                        break
                if continue_flag:
                    found_idx = path_idx_start + 1
                    break

            if found_idx == -1:
                return False
            patt_idx_start = patt_idx_tmp
            path_idx_start = found_idx + pat_len

        for i in range(patt_idx_start, patt_idx_end + 1):
            if patt_dirs[i] != "**":
                return False
        return True

    def __match_str(self, pattern: str, s: str) -> bool:

        def quote(s1: str, start: int, end_pos: int):
            if start == end_pos:
                return ""
            # re.escape 和 Pattern.quote作用类似
            return re.escape(s1[start:end_pos])

        matcher = re.finditer(glob_pattern, string=pattern)
        patt_str: str = ""
        end: int = 0
        for match in matcher:
            matched_str = match.group()
            patt_str += quote(pattern, end, match.start())
            if matched_str == "?":
                patt_str += "."
            elif matched_str == "*":
                patt_str += ".*"
            end = match.end()
        # 全文匹配
        if end == 0:
            return pattern == s
        patt_str += quote(pattern, end, len(pattern))
        reg = re.compile(patt_str)
        print(reg.match(s))
        return reg.fullmatch(s) is not None
