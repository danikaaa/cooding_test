function solution(s) {
    let slen = s.length/2;
    if(s.length % 2 == 0){
        return s[slen-1]+s[slen];
    }else{
        return s[Math.floor(slen)];
    }
}