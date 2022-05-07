/*
 * @lc app=leetcode id=146 lang=javascript
 *
 * [146] LRU Cache
 */

// @lc code=start
/**
 * @param {number} capacity
 * 
 * 队列知道最早的元素是哪一个
 * key item 映射 快速获取元素
 * 
 */
var LRUCache = function (capacity) {
  this.capacity = capacity
  this.keyMap = new Map()
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function (key) {
  if (this.keyMap.has(key)) {
    let value = this.keyMap.get(key)
    this.keyMap.delete(key)
    this.keyMap.set(key, value)
    return value
  } else {
    return -1
  }
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function (key, value) {
  if (this.keyMap.has(key)) {
    this.keyMap.delete(key)
    this.keyMap.set(key, value)
  } else {
    if (this.keyMap.size >= this.capacity) {
      this.keyMap.delete(this.keyMap.keys().next().value)
    }
    this.keyMap.set(key, value)
  }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
// @lc code=end

