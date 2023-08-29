function solution(a, b) {
    
    num = 0;
    if(a > b){
        for(let i = b+1; a > i; i++){
            num += i
        }
        return num+a+b;
    }else if(a < b){
        for(let i = a+1; b>i; i++){
            num += i
        }
        return num+a+b;
    }else{
        return a;
    }
}