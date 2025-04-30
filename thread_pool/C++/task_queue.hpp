#ifndef TASK_QUEUE_HPP
#define TASK_QUEUE_HPP

#include <pthread.h>
#include <queue>

// 任务结构体
using callback = void (*)(void *);
struct Task
{
    Task()
    {
        function = nullptr;
        arg = nullptr;
    }
    Task(callback f, void *arg)
    {
        function = f;
        this->arg = arg;
    }

    callback function;
    void *arg;
};

// 任务队列
class TaskQueue
{
private:
    pthread_mutex_t m_mutex;  // 互斥锁
    std::queue<Task> m_queue; // 任务队列
public:
    TaskQueue();
    ~TaskQueue();

    // 添加任务
    void addTask(Task &task);
    void addTask(callback f, void *arg);
    // 取出一个任务
    Task getTask();
    // 获取当前队列中任务个数
    inline int getTaskCount()
    {
        return m_queue.size();
    }
};

#endif