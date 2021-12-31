local heap = require 'src/heap'

describe('Heap', function()
  it('creates an empty heap', function()
    local h = heap.create()
    assert.equals(0, #h)
  end)

  it('has the right length', function()
    local h = heap.create({3, 2, 1, 5, 7})
    assert.equals(5, #h)
  end)

  it('extracts the minimum', function()
    local h = heap.create({3, 10, 1, 1000, 2000})

    local min = heap.pop_min(h)

    assert.equals(1, min)
    assert.equals(4, #h)
  end)

  it('fails to pop from empty heap', function()
    local h = heap.create({1})
    heap.pop_min(h)

    assert.has_error(function()
      heap.pop_min(h)
    end)
  end)

  it('inserts a new minimum', function()
    local h = heap.create({2, 3, 5, 7})

    heap.insert(h, 1)
    assert.equals(5, #h)
    local min = heap.pop_min(h)

    assert.equals(1, min)
    assert.equals(4, #h)
  end)

  it('pops many values in order', function()
    local h = heap.create({9, 7, 8, 6, 1, 5, 3, 2, 4})

    for i=1,9 do
      n = heap.pop_min(h)
      assert.equals(i, n)
    end
    assert.equals(0, #h)
  end)

  it('finds a value', function()
    local h = heap.create({19, 17, 18, 16, 11, 15, 13, 12, 14})

    local i, x = heap.find(h, 11)

    assert.equals(1, i)
    assert.equals(11, x)
  end)

  it('replaces a value at index', function()
    local h = heap.create({19, 17, 18, 16, 11, 15, 13, 12, 14})

    heap.replace(h, 5, 1)

    local min = heap.pop_min(h)
    assert.equals(1, min)
    assert.equals(8, #h)
  end)

  it('works with strings', function()
    local h = heap.create({'c', 'd', 'b', 'a'})

    assert.equals('a', heap.pop_min(h))
  end)

  it('works with nodes with a metatable', function()
    local h = heap.create({node('x', 2), node('y', 1), node('z', 3)})
    min = heap.pop_min(h)

    assert.equals('y', min.value)
  end)
end)

local mt = {__lt = function(a, b) return a.cost < b.cost end}

function node(v, c)
  local result = {value=v, cost=c}
  setmetatable(result, mt)
  return result
end
