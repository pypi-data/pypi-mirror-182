class Descriptor:

    def __init__(self, option, color):
        # foreground color
        colors = dict(
            black   = {"fg_code": 30, "bg_code": 40, "desc": "黑色", "alias": "black"},
            red     = {"fg_code": 31, "bg_code": 41, "desc": "红色", "alias": "red"},
            green   = {"fg_code": 32, "bg_code": 42, "desc": "绿色", "alias": "green"},
            yellow  = {"fg_code": 33, "bg_code": 43, "desc": "黄色", "alias": "yellow"},
            blue    = {"fg_code": 34, "bg_code": 44, "desc": "蓝色", "alias": "blue"},
            magenta = {"fg_code": 35, "bg_code": 45, "desc": "洋红", "alias": "magenta"},
            cyan    = {"fg_code": 36, "bg_code": 46, "desc": "青色", "alias": "cyan"},
            white   = {"fg_code": 37, "bg_code": 47, "desc": "白色", "alias": "white"})

        # text code
        text_modes = dict(
            default      = {"code": 0,  "desc": "默认", "alias": "default"},                      
            highlight    = {"code": 1,  "desc": "高亮", "alias": "highlight"},
            no_bold      = {"code": 22, "desc": "非粗体", "alias": "no_bold"},
            underline    = {"code": 4,  "desc": "下划线", "alias": "underline"},
            no_underline = {"code": 24, "desc": "非下划线", "alias": "no_underline"},
            flash        = {"code": 5,  "desc": "闪烁", "alias": "flash"},
            no_flash     = {"code": 25, "desc": "非闪烁", "alias": "no_flash"},
            reverse      = {"code": 7,  "desc": "反显", "alias": "reverse"},
            no_reverse   = {"code": 27, "desc": "非反显", "alias": "no_reverse"},
            no_visible   = {"code": 8,  "desc": "不可见", "alias": "no_visible"},
            visible      = {"code": 28, "desc": "可见", "alias": "visible"})

        self.option = option
        self.color  = color
        self.options = dict(colors=colors, text_modes=text_modes)
        self.null = {"fg_code": "", "bg_code": "", "code": "",  "desc": None, "alias": None}

    def __get__(self, instance, owner):
        if self.options.__contains__(self.option):
            if self.color is True:
                return self.options[self.option]
            else:
                return self.options[self.option].get(self.color, self.null)
        return self.null


class Attribute:
    black = Descriptor("colors", "black")
    red = Descriptor("colors", "red")
    green = Descriptor("colors", "green")
    yellow = Descriptor("colors", "yellow")
    blue = Descriptor("colors", "blue")
    magenta = Descriptor("colors", "magenta")
    cyan = Descriptor("colors", "cyan")
    white = Descriptor("colors", "white")

    # 显示模式
    default = Descriptor("text_modes", "default")
    highlight = Descriptor("text_modes", "highlight")
    no_bold = Descriptor("text_modes", "no_bold")
    underline = Descriptor("text_modes", "underline")
    no_underline = Descriptor("text_modes", "no_underline")
    flash = Descriptor("text_modes", "flash")
    no_flash = Descriptor("text_modes", "no_flash")
    reverse = Descriptor("text_modes", "reverse")
    no_reverse = Descriptor("text_modes", "no_reverse")
    no_visible = Descriptor("text_modes", "no_visible")
    visible = Descriptor("text_modes", "visible")

    null = Descriptor(None, None)
    colors = Descriptor("colors", True)
    text_modes = Descriptor("text_modes", True)


    def _initialization(self, fg, bg, mode):
        """\
        :params fg(foreground color): 前景色
        :params bg(background color): 背景色
        :params mode: 文本显示模式"""

        fg = self._parse_attr(fg, self.colors, "fg_code")
        bg = self._parse_attr(bg, self.colors, "bg_code")
        if isinstance(mode, (list, tuple)):
            mode = [self._parse_attr(item, self.text_modes, "code") for item in mode]
        else:
            mode = [self._parse_attr(mode, self.text_modes, "code")]

        return fg, bg, mode


    def _parse_attr(self, attr, attris, key):
        # dict
        if isinstance(attr, dict):
            if attr.__contains__(key) \
                and str(attr[key]).isdigit():

                for item in attris.values():
                    if int(attr[key]) == item[key]:
                        attr = item
                        break
                else:
                    attr = self.null
            else:
                attr = self.null

        # int
        elif isinstance(attr, int):
            for item in attris.values():
                if attr == item[key]:
                    attr = item
                    break
            else:
                attr = self.null

        # str
        else:
            # list or tuple
            if isinstance(attr, (list, tuple)) and attr:
                attr = attr[0]
            attr = str(attr).lower()

            for item in attris.values():
                if attr in (item["alias"], str(item[key]), item["desc"]):
                    attr = item
                    break
            else:
                attr = self.null
        return attr
