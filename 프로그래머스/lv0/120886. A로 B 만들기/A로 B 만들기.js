function solution(before, after) {
    const before_str = before.split("").sort().join("");
    const after_str = after.split("").sort().join("");
    return before_str == after_str ? 1 : 0;
}