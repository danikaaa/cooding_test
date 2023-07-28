function solution(my_string) {
    
    var rev ='';
    
    for(var i = 0; i< my_string.length; i++){
        rev = my_string[i]+rev;
    }
    
    return rev;
}