function solution(sides) {
    sides.sort((a,b) => b-a);
    sum = sides[1] + sides[2];
    return sum > sides[0] ? 1: 2;
}