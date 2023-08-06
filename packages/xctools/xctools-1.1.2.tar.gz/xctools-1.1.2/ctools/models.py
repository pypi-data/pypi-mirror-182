import math
from .colored import Colored


class ColorPrint(Colored):

    # 打印: 红色
    def print_red(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
        **kwargs
    ):
        rlt = self.colored(text, self.red, bg, mode, endmode=endmode)
        print(rlt, **kwargs)

    # 打印: 绿色
    def print_green(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
        **kwargs
    ):
        rlt = self.colored(text, self.green, bg, mode, endmode=endmode)
        print(rlt, **kwargs)

    # 打印: 蓝色
    def print_blue(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
        **kwargs):

        rlt = self.colored(text, self.blue, bg, mode, endmode=endmode)
        print(rlt, **kwargs)

    # 打印: 黄色
    def print_yellow(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
        **kwargs
    ):
        rlt = self.colored(text, self.yellow, bg, mode, endmode=endmode)
        print(rlt, **kwargs)

    # 打印: 洋红
    def print_magenta(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
        **kwargs
    ):
        rlt = self.colored(text, self.magenta, bg, mode, endmode=endmode)
        print(rlt, **kwargs)

    # 打印: 青色
    def print_cyan(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
        **kwargs
    ):
        rlt = self.colored(text, self.cyan, bg, mode, endmode=endmode)
        print(rlt, **kwargs)

    # 打印: 白色
    def print_white(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
        **kwargs
    ):
        rlt = self.colored(text, self.white, bg, mode, endmode=endmode)
        print(rlt, **kwargs)

    # 打印: 黑色
    def print_black(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
        **kwargs
    ):
        rlt = self.colored(text, self.black, bg, mode, endmode=endmode)
        print(rlt, **kwargs)

    # 着色: 红色
    def colored_red(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
    ):
        return self.colored(text, self.red, bg, mode, endmode=endmode)

    # 着色: 绿色
    def colored_green(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
    ):
        return self.colored(text, self.green, bg, mode, endmode=endmode)

    # 着色: 蓝色
    def colored_blue(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
        **kwargs):

        return self.colored(text, self.blue, bg, mode, endmode=endmode)

    # 着色: 黄色
    def colored_yellow(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
    ):
        return self.colored(text, self.yellow, bg, mode, endmode=endmode)

    # 着色: 洋红
    def colored_magenta(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
    ):
        return self.colored(text, self.magenta, bg, mode, endmode=endmode)

    # 着色: 青色
    def colored_cyan(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
    ):
        return self.colored(text, self.cyan, bg, mode, endmode=endmode)

    # 着色: 白色
    def colored_white(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
    ):
        return self.colored(text, self.white, bg, mode, endmode=endmode)

    # 着色: 黑色
    def colored_black(
        self,
        text: str,
        /,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
    ):
        return self.colored(text, self.black, bg, mode, endmode=endmode)

    def progress_bar(self, now, total , lenght=36, desc="", bar=b"\xe2\x94\x81", pad=""):
        """
        :params now: 当前进度值
        :params total: 总进度值
        :params lenght: 进度条长度
        :params desc: 进度条介绍
        :params bar: 进度条 进度填充
        params pad: 进度条 其余填充
        """
        now = total if now >= total else now
        bar = bar.decode() if isinstance(bar, bytes) else str(bar)
        percent = now / total
        total_bar = self.colored_green(lenght * bar)
        progress_bar = self.colored_green(
            math.floor(percent * lenght) * bar)
        percent = self.colored(f"{percent:.2%}", mode=self.underline)
        end = "\n" if now >= total else ""
        print(f"\r{desc}<{progress_bar:{pad}<{len(total_bar)}}> {percent} [{now}/{total}] ", end=end, flush=True)
