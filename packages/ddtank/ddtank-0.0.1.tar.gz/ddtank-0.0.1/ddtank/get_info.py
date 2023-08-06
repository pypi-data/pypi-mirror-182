import win32gui
import re

def get_windows_info():
    windows_list, info_list = [], []
    win32gui.EnumWindows(lambda w, param: param.append(w), windows_list)
    pattern_for_36 = re.compile(r'\[(.*)-(.*)-(.*)]\|(.*)\|(.*)\|(.*)\|(.*)\|(.*)')
    for window in windows_list:
        title = win32gui.GetWindowText(window)
        re_rst = pattern_for_36.search(title)
        if re_rst:
            rst = re_rst.groups()
            info_dict = {'platform': rst[0], 'service': int(rst[1]), 'name': rst[2], 'index': int(rst[3]), 'hwnd': int(rst[5])}
            info_list.append(info_dict)
    return info_list


