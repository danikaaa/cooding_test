function solution(arr) {
    
    let sum = 0;
    arr.forEach(function(e){
        sum += e;
    });
    
    return sum/arr.length;
}