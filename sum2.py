class Solution: 
  def summation(self, nums :list[int])->list[int]: 

      for i in range(10):
          number = int(input(f"Enter number {i+1} (consecutive number): "))
          nums.append(number)

      #Compute the sum of all the numbers
      sum_all_numbers = sum(nums)
      print(f"\nSum of all numbers: {sum_all_numbers}")
sol= Solution();
print(sol.summation([0,1,2,3,4,5,6,7,8,9]))