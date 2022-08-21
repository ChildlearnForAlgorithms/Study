# [덧셈, 뺄셈, 곱셈, 나눗셈]
import sys


def backtrack(k, res):
    global min_res, max_res
    if k > n - 1:
        if min_res > res:
            min_res = res
        if max_res < res:
            max_res = res
        return

    if exp[0] > 0:
        exp[0] -= 1
        backtrack(k + 1, res + nums[k])
        exp[0] += 1
    if exp[1] > 0:
        exp[1] -= 1
        backtrack(k + 1, res - nums[k])
        exp[1] += 1
    if exp[2] > 0:
        exp[2] -= 1
        backtrack(k + 1, res * nums[k])
        exp[2] += 1

    if exp[3] > 0:
        exp[3] -= 1
        backtrack(k + 1, (abs(res) // nums[k]) * (1 if res > 0 else -1))
        exp[3] += 1


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
exp = list(map(int, sys.stdin.readline().split()))
min_res = 1000000000
max_res = -1000000000
backtrack(1, nums[0])
print(max_res)
print(min_res)

'''
void loop(){  
    int cnt = 0;
    digitalWrite(13, HIGH);
    while(cnt<500){
        digitalWrite(trig, HIGH);
        delay(10);
        cnt= cnt + 10;
        digitalWrite(trig, LOW);
        int duration = pulseIn(echo, HIGH);
        int dis = duration / 29 / 2;
        if(dis<100){
            tone(10,494,10);
        }else{
            notone(10);
        }
    }
    digitalWrite(trig, LOW);
    digitalWrite(13, LOW); //빨간 led 꺼짐
    digitalWrite(12, HIGH); //초록 led켜짐
    delay(5000);
    digitalWrite(12,LOW); //초록 LED꺼짐
}
'''
