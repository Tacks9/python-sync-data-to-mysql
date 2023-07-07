from tasks.category import handleInsert
import schedule
import time
import threading


def main():
    # 每隔 1 秒钟执行一次任务
    schedule.every(1).seconds.do(handleInsert)

    # 无限循环来不断检查定时任务是否应该执行
    while True:
        # 执行任务
        schedule.run_pending()

        # 获取当前线程列表
        threads = threading.enumerate()
        # 打印线程信息
        print("当前线程列表:")
        for t in threads:
            print(t)

        # 休息一下
        time.sleep(1)

if __name__ == '__main__':
    main()