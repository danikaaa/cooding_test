function solution(numbers, num1, num2) {
    let t = 0
    t = num2-num1;
    return numbers.splice(num1,t+1);
}