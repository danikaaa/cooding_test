function solution(sides) {
    sides.sort((a,b) => b-a);
    sum = sides[1] + sides[2];
    if(sum > sides[0]){
        return 1;
    }else{
        return 2;
    }
    
}