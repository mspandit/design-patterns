class NotSingleton
  def self.instance
    return NotSingleton.new
  end
end


class Singleton

  def Singleton.instance
    unless @@unique_instance
      @@unique_instance = new
    end
    return @@unique_instance
  end
  
  private_class_method :new
  
  private
  
  @@unique_instance = nil

end


ns1 = NotSingleton.instance
puts "ns1 = #{ns1}"
ns2 = NotSingleton.instance
puts "ns2 = #{ns2}"

ns1 = NotSingleton.new
puts "ns1 = #{ns1}"
ns2 = NotSingleton.new
puts "ns2 = #{ns2}"

s1 = Singleton.instance
puts "s1 = #{s1}"
s2 = Singleton.instance
puts "s2 = #{s2}"

s1 = Singleton.new