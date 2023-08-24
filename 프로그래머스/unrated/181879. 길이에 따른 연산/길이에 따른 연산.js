function solution(num_list) {
    num = 0;
    num2= 1;
    if(num_list.length >= 11){
        for(let i = 0; num_list.length > i; i++){
            num += num_list[i];
        }
        return num;
    }else{
       for(let i = 0; num_list.length > i; i++){
            console.log(num_list[i]);
            num2 = num2 * num_list[i];
        } 
        return num2;
    }
}