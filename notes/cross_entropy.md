Cross-entropy is a commonly used loss function for classification tasks.
However, there are differnt versions of cross entropy loss in the machine learning context.
* General forula for cross-entropy loss  

$$
\text{ cross entropy loss } = -\sum_{x=1}^m p_x \cdot log (q_x)
$$  

Where m is the total number of classes in the classification problem, $p_x$ is the true probability (ground truth) for the class x and $q_x$ is the prediction for the class x. 

* Special case - categorical cross entropy loss  

$$
\text{ categorical cross entropy loss } = -  log (q_x)
$$  

Where the target is now a one hot vector, x is the class with 1 in the one hot vector. Due to the one hot vector encoding, other classes are clancelled out in the general formula.  


* Special case - binary corss entropy loss for one particular class (class x in this case)  

$$  
\text{ binary cross entropy loss } = - [ p_x \cdot log (q_x) + (1 - p_x) \cdot log (1 - q_x)] 
$$  

Where x is the considered class, this loss now consideres  if our target is either 0 or 1. For exmple to predict whether the image contains a panda or not.  

* Special case - binary corss entropy loss, usage for many classes  

$$  
\text{ loss } = \sum_{x=1}^m - [ p_x \cdot log (q_x) + (1 - p_x) \cdot log (1 - q_x)] 
$$  