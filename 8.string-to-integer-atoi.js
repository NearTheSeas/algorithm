/*
 * @lc app=leetcode id=8 lang=javascript
 *
 * [8] String to Integer (atoi)
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */

const START = 'start'
const SIGNED = 'signed'
const INNUMBER = 'in_number'
const END = 'end'
var myAtoi = function (s) {
  class Automaton {
    constructor() {
      this.state = START
      this.sign = 1
      this.ans = 0
      this.stateMap = new Map([
        [START, [START, SIGNED, INNUMBER, END]],
        [SIGNED, [END, END, INNUMBER, END]],
        [INNUMBER, [END, END, INNUMBER, END]],
        [END, [END, END, END, END]],
      ])
    }

    getStateIndex(char) {
      if (char === ' ') {
        return 0
      } else if (char === '-' || char === '+') {
        return 1
      } else if (typeof Number(char) === 'number' && !isNaN(char)) {
        return 2
      } else {
        return 3
      }
    }

    get(char) {
      this.state = this.stateMap.get(this.state)[this.getStateIndex(char)]
      if (this.state === INNUMBER) {
        this.ans = this.ans * 10 + (char - 0)
        this.ans = this.sign === 1 ? Math.min(this.ans, Math.pow(2, 31)) : Math.min(this.ans, -Math.pow(-2, 31))
      } else if (this.state === SIGNED) {
        this.sign = char === '+' ? 1 : -1
      }
    }
  }
  let auomation = new Automaton()
  for (let char of s) {
    auomation.get(char)
  }

  return auomation.sign * auomation.ans

};
// @lc code=end

