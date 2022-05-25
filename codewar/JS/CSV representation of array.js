function toCsvText(arr) {
    // P array
    // R String
    // E input:
  //    [[ 0, 1, 2, 3, 4 ],
  //     [ 10,11,12,13,14 ],
  //     [ 20,21,22,23,24 ],
  //     [ 30,31,32,33,34 ]] 
      
  // output:
  //      '0,1,2,3,4\n'
  //     +'10,11,12,13,14\n'
  //     +'20,21,22,23,24\n'
  //     +'30,31,32,33,34'
    // P
    // 1 loop over array
    // 2 add each to string
    return arr.join("\n")
  }