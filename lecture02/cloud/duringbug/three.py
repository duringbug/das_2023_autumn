'''
Description: 
Author: 唐健峰
Date: 2023-09-25 17:58:58
LastEditors: ${author}
LastEditTime: 2023-09-25 20:03:35
'''

import queue

elements = {}
elements["man"] = [["man", "sheep", "wolf", "greens"],
                   ["man", "wolf",  "greens"], ["man", "sheep", "wolf"], ["man", "sheep",  "greens"], ["man", "sheep"]]
elements["wolf"] = [["wolf", "greens"], ["wolf"]]
elements["greens"] = [["greens"]]
elements["sheep"] = [["sheep"]]
elements[""] = [[""]]
graph = {}
graph["man_0"] = ["wolf_0"]
graph["man_1"] = ["wolf_0", "wolf_1", "greens_0"]
graph["man_2"] = ["wolf_1", "greens_0", "sheep_0"]
graph["man_3"] = ["greens_0", "sheep_0"]
graph["man_4"] = ["sheep_0", ""]
graph["wolf_0"] = ["man_0", "man_1"]
graph["wolf_1"] = ["man_1", "man_2"]
graph["greens_0"] = ["man_1", "man_2", "man_3"]
graph["sheep_0"] = ["man_2", "man_3", "man_4"]
graph[""] = ["man_4"]


def three():
    status = {}
    status["man_0"] = 1
    status["man_1"] = 0
    status["man_2"] = 0
    status["man_3"] = 0
    status["man_4"] = 0
    status["wolf_0"] = 0
    status["wolf_1"] = 0
    status["greens_0"] = 0
    status["sheep_0"] = 0
    status[""] = 0
    # 从graph[""]到达graph["man_0"]状态
    print_path("man_0", "man_0", status)
    return 0


def print_path(s, all_path, status):
    if s == "":
        my_list = all_path.split(" ")
        print("原岸状态:", end=": ")
        for s in my_list:
            if s != "":
                list_2 = s.split("_")
                print(elements[list_2[0]][int(list_2[1])], end=" ")
        print()
    else:
        for i in range(len(graph[s])):
            if status[graph[s][i]] == 0:
                print_path(graph[s][i], all_path+" " +
                           graph[s][i], mark_status(status, graph[s][i]))


def mark_status(status, s):
    status_copy = status.copy()
    status_copy[s] = 1
    return status_copy
