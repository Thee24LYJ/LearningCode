#pragma once

#include <iostream>
#include <queue>
#include <pthread.h>

#define NUM 5

template <class T>
class ThreadPool
{
private:
	int thread_num;
	std::queue<T> task_q;

	pthread_mutex_t lock;
	pthread_cond_t cond;

public:
	ThreadPool(int num = NUM) : thread_num(num)
	{
		pthread_mutex_init(&lock, nullptr);
		pthread_cond_init(&cond, nullptr);
	}

	~ThreadPool()
	{
		pthread_mutex_destroy(&lock);
		pthread_cond_destroy(&cond);
	}

public:
	void InitTheadPool()
	{
		pthread_t tid;
		for (int i = 0; i < thread_num; ++i)
		{
			pthread_create(&tid, nullptr, Routine, this); // !!
		}
	}

	static void *Routine(void *arg)
	{
		pthread_detach(pthread_self());
		ThreadPool *self = (ThreadPool *)arg;
		while (true)
		{
			self->Lock();
			while (self->IsEmpty())
			{
				self->Wait();
			}

			// 走到这里一定有任务
			T task;
			self->Pop(task);
			self->Unlock();

			// 有些任务处理时间可能较长，解锁之后再处理，否则就成串行了
			task.Run();
		}
	}

public:
	void Push(const T &in)
	{
		Lock();
		task_q.push(in);
		Unlock();

		Wakeup();
	}

	void Pop(T &out)
	{
		out = task_q.front();
		task_q.pop();
	}

	void Lock()
	{
		pthread_mutex_lock(&lock);
	}

	void Unlock()
	{
		pthread_mutex_unlock(&lock);
	}

	void Wait()
	{
		pthread_cond_wait(&cond, &lock);
	}

	void Wakeup()
	{
		pthread_cond_signal(&cond);
	}

	bool IsEmpty()
	{
		return task_q.size() == 0 ? true : false;
	}
};