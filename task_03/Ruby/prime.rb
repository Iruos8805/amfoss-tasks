
def is_prime?(number)
    return false if number <= 1
  
    (2..Math.sqrt(number)).none? { |i| (number % i).zero? }
  end

  print "Enter a number (n): "
  n = gets.chomp.to_i
  
  
  puts "Prime numbers up to #{n}:"
  (2..n).each { |num| puts num if is_prime?(num) }
  