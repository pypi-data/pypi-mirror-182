def results_plot(quiz):
	import matplotlib.pyplot as plt

	array = []
	length = quiz.quiz_length
	for i in range(length):
		array.append(quiz.QAs[i].mark)

	if (quiz.results == "off"):
		print("Cannot print results if results was set to \'off\'. \n")
		return
	if array.count('y') + array.count('n') == 0:
		pass
	else:

		plotting = [array.count('y'), array.count('n')]

		print("Right:", plotting[0])
		print("Wrong:", plotting[1])
		print("Grade:", round(plotting[0]/length * 100), "%")

		plt.pie(plotting, labels = ['Right', 'Wrong'])
		plt.show()
