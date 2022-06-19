function solution(clothes) {
  let answer = 1;
  let obj = {};

  clothes.forEach((c) => {
    obj[c[1]] = obj[c[1]] ? obj[c[1]] + 1 : 1;
    return obj;
  });

  for (let k in obj) {
    answer *= obj[k] + 1;
  }

  return answer - 1;
}

const example = [
  ["yellowhat", "headgear"],
  ["bluesunglasses", "eyewear"],
  ["green_turban", "headgear"],
];
const result = solution(example);
console.log(result);
