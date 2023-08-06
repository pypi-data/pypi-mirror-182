from .cattrs import Attribute


class Colored(Attribute):

    def colored(
        self,
        text: str,
        /,
        fg: str or dict=None,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True
    ):
        """
        :params text: 文本
        :params fg(foreground color): 前景色
        :params bg(background color): 背景色
        :params mode: 文本显示模式
        :params endmode: 当前文本着色, 后续文本恢复默认颜色(ture[default]/false)

        return colored_text

        Example:
            from ctools import cp

            r = cp.colored(
                "Hello World!",
                cp.fg_red,
                cp.bg_black,
                mode=[cp.highlight]
            )
            print(r)

            cp.cprint(
                "Hello World!",
                cp.fg_green,
                cp.bg_black,
                mode=[cp.highlight, cp.underline]
            )"""

        fg, bg, mode = self._initialization(fg, bg, mode)
        text = "\033[{mode};{fg};{bg};m{text}{endmode}".format(
            mode = ";".join([str(item["code"]) for item in mode]),
            fg = fg["fg_code"],
            bg = bg["bg_code"],
            text = text,
            endmode = "\033[0m" if endmode else "")
        return text

    def cprint(
        self,
        text: str,
        /,
        fg: str or dict=None,
        bg: str or dict=None,
        mode: str or list=None,
        *,
        endmode: bool=True,
        **kwargs
    ):
        rlt = self.colored(text, fg, bg, mode, endmode=endmode)
        print(rlt, **kwargs)
