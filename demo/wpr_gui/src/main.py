# coding=utf-8
#from tkinter import *
from Tkinter import *
import tkFont
#import tkinter.font as tkFont
import os
import pytalker as pyt

bash_path = " ~/Documents/demo/devel/setup.bash"

main_win = Tk()
main_win.title("简易机器人GUI界面")
main_win.geometry("200x500")


def create_map():
    map_win = Tk()
    map_win.title("建图")
    map_win.geometry("1000x1000")

    def mapping_start():
        pyt.mapping_start()

    def mapping_end():
        pyt.mapping_end()

    def save_map():
        global save_file
        save_win = Tk()
        save_win.title("保存地图")
        save_win.geometry("400x400")

        save_file = StringVar()
        save_win_en = Entry(save_win, textvariable=save_file)
        save_win_en.place(relx=0.5, rely=0.5, anchor='center')

        def save():
            pyt.save_map(save_win_en.get())

        save_bt = Button(save_win, text="OK", command=save)
        save_bt.place(relx=0.5, rely=0.6, anchor='center')

    def list_map():
        pyt.list_map()

    def delete_map():
        global delete_file
        delete_win = Tk()
        delete_win.title("删除地图")
        delete_win.geometry("400x400")

        delete_file = StringVar()
        delete_win_en = Entry(delete_win, textvariable=delete_file)
        delete_win_en.place(relx=0.5, rely=0.5, anchor='center')

        def delete():
            pyt.delete_map(delete_win_en.get())

        delete_bt = Button(delete_win, text="OK", command=delete)
        delete_bt.place(relx=0.5, rely=0.6, anchor='center')

    def load_map():
        global load_file
        load_win = Tk()
        load_win.title("加载地图")
        load_win.geometry("400x400")

        load_file = StringVar()
        load_win_en = Entry(load_win, textvariable=load_file)
        load_win_en.place(relx=0.5, rely=0.5, anchor='center')

        def load():
            pyt.load_map(load_win_en.get())

        load_bt = Button(load_win, text="OK", command=load)
        load_bt.place(relx=0.5, rely=0.6, anchor='center')

    def unload_map():
        pyt.unload_map()

    map_ft = tkFont.Font(size=20)
    map_stop_bt = Button(map_win, text="停止建图",
                         font=map_ft, command=mapping_end)
    map_stop_bt.place(relx=0.3, rely=0.7, anchor='center',
                      relwidth=0.15, relheight=0.08)

    map_start_bt = Button(map_win, text="开始建图", font=map_ft,
                          command=mapping_start)
    map_start_bt.place(relx=0.5, rely=0.7, anchor='center',
                       relwidth=0.15, relheight=0.08)

    map_save_bt = Button(map_win, text="保存地图", font=map_ft, command=save_map)
    map_save_bt.place(relx=0.7, rely=0.7, anchor='center',
                      relwidth=0.15, relheight=0.08)

    list_map_bt = Button(map_win, text="列出所有地图", font=map_ft, command=list_map)
    list_map_bt.place(relx=0.3, rely=0.8, anchor='center',
                      relwidth=0.15, relheight=0.08)

    delete_map_bt = Button(map_win, text="删除地图",
                           font=map_ft, command=delete_map)
    delete_map_bt.place(relx=0.7, rely=0.8, anchor='center',
                        relwidth=0.15, relheight=0.08)

    load_map_bt = Button(map_win, text="加载地图", font=map_ft, command=load_map)
    load_map_bt.place(relx=0.5, rely=0.8, anchor='center',
                      relwidth=0.15, relheight=0.08)

    unload_map_bt = Button(map_win, text="卸载地图",
                           font=map_ft, command=unload_map)
    unload_map_bt.place(relx=0.5, rely=0.9, anchor='center',
                        relwidth=0.15, relheight=0.08)


def nav():
    os.system("roslaunch wpr_navigation view_navigation.launch &")
    
    # nav_win = Tk()
    # nav_win.title("导航")
    # nav_win.geometry("1000x1000")

    # def nav_start():
    #     import os
    #     # pyt.nav_start(0.0 , 0.0, 0.0)
    #     os.system("roslaunch wpr_navigation view_navigation.launch &")

    # def nav_cancel():
    #     pass
    #     import os
    #     os.system("rosnode list | grep rviz | xargs -I {} rosnode kill {} &")
    #     # pyt.nav_cancel()

    # nav_ft = tkFont.Font(size=20)
    # nav_start_bt = Button(nav_win, text="开始导航", font=nav_ft, command=nav_start)
    # nav_start_bt.place(relx=0.4, rely=0.7, anchor='center',
    #                    relwidth=0.15, relheight=0.08)

    # nav_cancel_bt = Button(nav_win, text="关闭导航",
    #                        font=nav_ft, command=nav_cancel)
    # nav_cancel_bt.place(relx=0.6, rely=0.7, anchor='center',
    #                     relwidth=0.15, relheight=0.08)


def obj():
    obj_win = Tk()
    obj_win.title("抓取目标")
    obj_win.geometry("1000x1000")

    def grab():
        pyt.grab_start()

    def release():
        pyt.release_start()

    obj_ft = tkFont.Font(size=20)
    obj_grab_bt = Button(obj_win, text="抓取", font=obj_ft, command=grab)
    obj_grab_bt.place(relx=0.4, rely=0.7, anchor='center',
                      relwidth=0.15, relheight=0.08)

    obj_release_bt = Button(obj_win, text="释放", font=obj_ft, command=release)
    obj_release_bt.place(relx=0.6, rely=0.7, anchor='center',
                         relwidth=0.15, relheight=0.08)


def barrier():
    barrier_win = Tk()
    barrier_win.title("避障")
    barrier_win.geometry("100x220")

    def start():
        pyt.barrier_start()

    def stop():
        pyt.barrier_end()

    barrier_ft = tkFont.Font(size=20)
    start_bt = Button(barrier_win, text="开启避障", font=barrier_ft, command=start)
    start_bt.place(relx=0.5, rely=0.3, anchor='center',
                   relwidth=0.85, relheight=0.4)

    stop_bt = Button(barrier_win, text="关闭避障", font=barrier_ft, command=stop)
    stop_bt.place(relx=0.5, rely=0.7, anchor='center',
                  relwidth=0.85, relheight=0.4)


def voice():
    voice_win = Tk()
    voice_win.title("语音控制")
    voice_win.geometry("1000x1000")

    def start():
        pyt.voice_start()

    def stop():
        pyt.voice_end()

    voice_ft = tkFont.Font(size=20)
    start_bt = Button(voice_win, text="开始聆听", font=voice_ft, command=start)
    start_bt.place(relx=0.4, rely=0.7, anchor='center',
                   relwidth=0.15, relheight=0.08)

    stop_bt = Button(voice_win, text="停止", font=voice_ft, command=stop)
    stop_bt.place(relx=0.6, rely=0.7, anchor='center',
                  relwidth=0.15, relheight=0.08)


def init_system():
    import os
    os.system('gnome-terminal -x bash -c "roslaunch wpr_simulation wpb_simple.launch;exec bash;" ')
    os.system('gnome-terminal -x bash -c "bash master.sh;exec bash;" ')
    os.system('gnome-terminal -x bash -c "bash mapMag.sh;exec bash;" ')
    pyt.init()


def manual_ctrl():
    import os
    os.system('gnome-terminal -x bash -c "rosrun vel_pkg key_move;exec bash;" ')


# def forward():
#     pyt.go_forward()

# def left():
#     pyt.turn_left()

# def right():
#     pyt.turn_right()

# def backward():
#     pyt.go_backward()

# def speed_up():
#     pyt.linear_speedup()


# def speed_down():
#     pyt.linear_speeddown()

# def angular_speed_up():
#     pyt.angular_speedup()

# def angular_speed_down():
#     pyt.angular_speeddown()

# def stop_move():
#     pyt.move_stop()
ft_function = tkFont.Font(size=15)
bt_map = Button(main_win, text="地图管理", font=ft_function, command=create_map)
bt_map.place(relx=0.50, rely=0.51, anchor='center',
             relwidth=0.55, relheight=0.10)

bt_nav = Button(main_win, text="自主导航", font=ft_function, command=nav)
bt_nav.place(relx=0.5, rely=0.64, anchor='center',
             relwidth=0.55, relheight=0.10)

bt_obj = Button(main_win, text="目标抓取", font=ft_function, command=obj)
bt_obj.place(relx=0.5, rely=0.77, anchor='center',
             relwidth=0.55, relheight=0.10)

bt_init = Button(main_win, text="开机", font=ft_function, command=init_system)
bt_init.place(relx=0.25, rely=0.1, anchor='center',
              relwidth=0.30, relheight=0.08)

bt_init = Button(main_win, text="障碍检测", font=ft_function, command=barrier)
bt_init.place(relx=0.50, rely=0.38, anchor='center',
              relwidth=0.55, relheight=0.10)

# bt_voice = Button(main_win, text="语音控制", font=ft_function, command=voice)
# bt_voice.place(relx=0.5, rely=0.5, anchor='center',
#                relwidth=0.15, relheight=0.08)

bt_stop = Button(main_win, text="手动控制", font=ft_function, command=manual_ctrl)
bt_stop.place(relx=0.50, rely=0.25, anchor='center',
              relwidth=0.55, relheight=0.10)


ft_direction = tkFont.Font(size=15)

# bt_left = Button(main_win, text="左转", font=ft_direction, command=left)
# bt_left.place(relx=0.35, rely=0.7, anchor='center', relwidth=0.1, relheight=0.05)


# bt_right = Button(main_win, text="右转", font=ft_direction, command=right)
# bt_right.place(relx=0.65, rely=0.7, anchor='center', relwidth=0.1, relheight=0.05)

# bt_forward = Button(main_win, text="前进", font=ft_direction, command=forward)
# bt_forward.place(relx=0.5, rely=0.6, anchor='center', relwidth=0.1, relheight=0.05)

# bt_backward = Button(main_win, text="后退", font=ft_direction, command=backward)
# bt_backward.place(relx=0.5, rely=0.8, anchor='center', relwidth=0.1, relheight=0.05)

# bt_speed_up = Button(main_win, text="加速移动", font=ft_direction, command=speed_up)
# bt_speed_up.place(relx=0.8, rely=0.7, anchor='center', relwidth=0.1, relheight=0.05)

# bt_speed_down = Button(main_win, text="减速移动", font=ft_direction, command=speed_down)
# bt_speed_down.place(relx=0.8, rely=0.8, anchor='center', relwidth=0.1, relheight=0.05)

# bt_angular_speed_up = Button(main_win, text="加速转向", font=ft_direction, command=angular_speed_up)
# bt_angular_speed_up.place(relx=0.2, rely=0.7, anchor='center', relwidth=0.1, relheight=0.05)

# bt_angular_speed_down = Button(main_win, text="减速转向", font=ft_direction, command=angular_speed_down)
# bt_angular_speed_down.place(relx=0.2, rely=0.8, anchor='center', relwidth=0.1, relheight=0.05)

ft_Inf = tkFont.Font(size=15)
l_Inf = Label(main_win, font=ft_Inf, text="Team 204")
l_Inf.place(relx=0.5, rely=0.95, anchor='center', relwidth=0.5, relheight=0.05)
main_win.mainloop()
