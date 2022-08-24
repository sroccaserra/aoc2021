// @ts-check
import { readFileSync } from 'fs'

function solve_09_1(floorMap) {
  let result = 0
  for (const point of floorMap.findLowPoints()) {
    result += floorMap.riskAt(point.i, point.j)
  }
  return result
}

class FloorMap {
  constructor(lines) {
    this.lines = lines
    this.w = lines[0].length
    this.h = lines.length
  }

  findLowPoints() {
    const result = []
    for (let i = 0; i < this.h; i++) {
      for (let j = 0; j < this.w; j++) {
        if (this.isLowPoint(i, j)) {
          result.push({i: i, j: j})
        }
      }
    }
    return result
  }

  isLowPoint(i, j) {
    const c = this.charAt(i, j)
    for (const n of this.neighbors(i, j)) {
      if (this.charAt(n.i, n.j) <= c) {
        return false
      }
    }
    return true
  }

  charAt(i, j) {
    return this.lines[i][j]
  }

  neighbors(i, j) {
    const result = []
    if (0 < i) {
      result.push({i: i-1, j})
    }
    if (i < this.h-1) {
      result.push({i: i+1, j})
    }
    if (0 < j) {
      result.push({i, j: j-1})
    }
    if (j < this.w-1) {
      result.push({i, j: j+1})
    }
    return result
  }

  riskAt(i, j) {
    return 1+ Number(this.charAt(i, j))
  }
}

const file = readFileSync(process.argv[2], 'utf8')
const lines = file.split('\n').slice(0, -1)
const floorMap = new FloorMap(lines)

console.log(solve_09_1(floorMap))
