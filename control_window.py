#coding=utf8
#Author:Guo Xiangchen

import multiprocessing
from time import sleep
import do_show_maidian

#if __name__ == "__main__":
def control_window():
	manager = multiprocessing.Manager()
	stop_flag = manager.list()
	print (len(stop_flag))

	# Define a list (queue) for tasks and computation results
	tasks = manager.Queue()
	results = manager.Queue()

	# Creat process pool with four porcesses
	num_processes = 2
	pool = multiprocessing.Pool(processes = num_processes)
	processes = []

	# Initiate the worker processes
	#for i in range(num_processes):
	# Set process name
		#process_name = 'P%i' % i
	process_name = "P0"
	process_name1 = "P1"

	# Create the process, and connect it to the worker function
	watch_mysql_pro = multiprocessing.Process(target = do_show_maidian.watch_mysql, args = (process_name, tasks, results, stop_flag))
	match_result_pro = multiprocessing.Process(target = do_show_maidian.match_result, args = (process_name1, tasks, results, stop_flag,))
	#new_process2 = multiprocessing.Process(target= check_app.check_app ,args=())

	# Add new process to the list of processes
	processes.append(watch_mysql_pro)
	print (processes)
	processes.append(match_result_pro)
	print (processes)

	# Start the process
	watch_mysql_pro.start()
	print("watch_mysql_pro START !")



	# Fill task queue
	#task_list = [43, 1, 780, 256, 142, 68, 183, 334, 325, 3]
	#for single_task in task_list:
		#tasks.put(single_task)

	# Wait while the workers process
	sleep(3)

	# Quit the worker processes by sending them -1
	#for i in range(num_processes):
		#tasks.put(-1)

	# Read calculation results
	num_finished_processes = 0
	while True:
		# Read result
		new_result = results.get()

		# Have a look at the results
		if new_result == 1:
			# Process has finished
			match_result_pro.start()
			print("match_result_pro START !")
			watch_mysql_pro.start()
			print("watch_mysql_pro START !")
			#num_finished_processes += 1

			#if num_finished_processes == num_processes:
				#break
		else:
			# Output result
			print ('Result:' + str(new_result))

if __name__ == '__main__':
	print("!!")
	control_window()