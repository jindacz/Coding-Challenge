var findAverage = function (nums) {
    // P array
    // R number average of array
    // E findAverage([1, 3, 5, 7]), 4
    // P
    let sum = nums.reduce((acc, curr) => acc + curr, 0)
    return sum / nums.length
  }