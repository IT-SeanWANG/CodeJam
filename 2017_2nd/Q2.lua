#!/usr/bin/lua 

--[[
	write by Sean WANG
	environment: Windows 7 Lua5.1.5
	2017/04/22
]]--

-- convert string to table
function string.split(str, delimiter)
	if str==nil or str=='' or delimiter==nil then
		return nil
	end
	
    local result = {}
    for match in (str..delimiter):gmatch("(.-)"..delimiter) do
        table.insert(result, match)
    end
    return result
end


-- main function
product_num = tonumber(io.read())

-- create & input profit matrix
profit_matrix = {}
for i = 1, product_num do
	profit_matrix[i] = {}
end
for i = 1, product_num do
	profit_str = io.read()
	-- construct profit matrix
	profit_matrix[i] = string.split(profit_str, " ")
end

-- calc max profit
max_profit = 0
cnt = 0
tmp_i = 0
tmp_j = 0
while cnt < math.floor(product_num/2) do
	max = 0
	for i = 1, product_num do
		for j = 1, i do
			if tonumber(profit_matrix[i][j]) > max then
				tmp_i = i
				tmp_j = j
				max = tonumber(profit_matrix[i][j])
			end
		end
	end
	cnt = cnt + 1
	max_profit = max_profit + max
	-- set the related row and col to 0
	for i = 1, product_num do
		for j = 1, i do
			if (i == tmp_i) or (j == tmp_i) or (i == tmp_j) or (j == tmp_j) then
				profit_matrix[i][j] = 0
			end
		end
	end
end
print(max_profit)
