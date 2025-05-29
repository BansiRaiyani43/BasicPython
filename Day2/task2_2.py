"""
In cricket, an over consists of six deliveries a bowler bowls from one end. Create a program that takes the number of balls 
bowled by a bowler and calculates the number of overs and balls bowled by him/her. Return the value as a float, in the format 
overs.balls.
"""
def balls_overs(total_balls):
    overs = total_balls // 6
    balls = total_balls % 6
    return float(f"{overs}.{balls}")

print(balls_overs(15))
print(balls_overs(24))
print(balls_overs(5))