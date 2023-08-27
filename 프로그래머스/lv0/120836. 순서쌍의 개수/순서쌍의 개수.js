function solution(n) {
    let num = 0;
    for(let i=0; i <= n; i++){
        if(n%i === 0){
            num++
        }
    }
    return num;
}