require "Time"

dt = "2019-04-04"
puts Time.parse(dt)

arr = []

Array(1..3).each do |i|
  arr << i ** 2
end

puts arr
puts arr.class
