import prob_calculator

hat1 = prob_calculator.Hat(black=6, red=4, green=3)

probability = prob_calculator.experiment(
	hat=hat1, 
	expected_balls={"red":2,"green":1}, 
	num_balls_drawn=5, 
	num_experiments=10000)

print("Probability: ", probability)