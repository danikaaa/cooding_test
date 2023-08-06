function solution(start, end) {
    var arr = [];
    for(let i = start; i >= end; i--){
        arr.push(i);
    }
    return arr;
}