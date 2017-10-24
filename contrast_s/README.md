# Contrast Sets

## Descriptions:

Our contrast learner will examine each pair of nodes in the decision tree and report the delta and effect between each node in a pair:

+ The delta is the difference in the branch path between each node
+ The effect is the mean difference in the performance score those nodes

Note that if the delta is:

+ positive then the contrast is a plan (something to do).
+ negative then the contrast is a monitor (something to watch for).

Note also that is statistically there is no difference between the population of instances in each node, then there is no point printing that contrast. 
