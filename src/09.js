import { getInputLines, Queue } from './common/common.js'

function solve_09_1(floorMap) {
  let result = 0
  for (const point of floorMap.findLowPoints()) {
    result += floorMap.riskAt(point)
  }
  return result
}

function solve_09_2(floorMap) {
  const basinSizes = []
  for (const point of floorMap.findLowPoints()) {
    basinSizes.push(floorMap.basinSizeAt(point))
  }
  basinSizes.sort((a, b) => b - a)
  return basinSizes[0] * basinSizes[1] * basinSizes[2]
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
        if (this.isLowPoint({i, j})) {
          result.push({i, j})
        }
      }
    }
    return result
  }

  isLowPoint(point) {
    const c = this.charAt(point)
    for (const n of this.neighbors(point)) {
      if (this.charAt(n) <= c) {
        return false
      }
    }
    return true
  }

  charAt({i, j}) {
    return this.lines[i][j]
  }

  neighbors({i, j}) {
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

  riskAt(point) {
    return 1 + Number(this.charAt(point))
  }

  basinSizeAt(lowPoint) {
    let result = 0
    const known = {}
    const q = new Queue()

    function process(point) {
      result += 1
      q.enqueue(point)
      known[`${point.i}_${point.j}`] = true
    }

    process(lowPoint)
    while (q.size() > 0 ) {
      const point = q.dequeue()
      for (const n of this.flowingNeighbors(point)) {
        if (!known[`${n.i}_${n.j}`]) {
          process(n)
        }
      }
    }
    return result
  }

  flowingNeighbors(point) {
    const c = this.charAt(point)

    const result = []
    for (const n of this.neighbors(point)) {
      const neighborChar = this.charAt(n)
      if (c < neighborChar && '9' != neighborChar) {
        result.push(n)
      }
    }
    return result
  }
}

const lines = getInputLines()
const floorMap = new FloorMap(lines)

console.log(solve_09_1(floorMap))
console.log(solve_09_2(floorMap))
