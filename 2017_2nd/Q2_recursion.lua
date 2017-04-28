#!/usr/bin/lua

--[[
	write by Sean WANG
	environment: Windows 7 Lua5.1.5
	2017/04/22
]]--


-- deep copy
function clone(object)
	local lookup_table = {}
	local function _copy(object)
		if type(object) ~= "table" then
			return object
		elseif lookup_table[object] then
			return lookup_table[object]
		end
	local newObject = {}
		lookup_table[object] = newObject
		for key, value in pairs(object) do
			newObject[_copy(key)] = _copy(value)
		end
		return setmetatable(newObject, getmetatable(object))
	end
	return _copy(object)
end

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

-- choice one table value and set corresponding row/col to 0
function table_deal(tmp_table, num)
	local loc_value = 0
	local loc_i = 0
	local loc_j = 0
	for i = num, 2, -1 do
		for j = i - 1, 1, -1 do
			if tonumber(tmp_table[i][j]) > 0 then
				loc_value = tonumber(tmp_table[i][j])
				loc_i = i
				loc_j = j
				break
			end
		end
		if loc_value > 0 then
			break
		end
	end
	-- set the related row and col to 0
	for i = 1, num do
		for j = 1, i do
			if (i == loc_i) or (j == loc_i) or (i == loc_j) or (j == loc_j) then
				profit_matrix[loc_i][loc_j] = 0
			end
		end
	end
	return loc_value
end

-- recursion to calc max profit
function recursion_calc(input_table, base_num, choice_num, output_table, combine_num)
	local loc_tmp_max = 0
	local loc_max = 0

	if choice_num == 0 then
		for i = 1, combine_num do
			loc_tmp_max = loc_tmp_max + output_table[i]
		end
		if loc_tmp_max > loc_max then
			loc_max = loc_tmp_max
		end
		input_table = clone(profit_matrix)
	end

	for i = base_num, choice_num, -1 do
		output_table[choice_num] = table_deal(input_table, base_num)
		recursion_calc(input_table, base_num - 1, choice_num -1, output_table, combine_num)
	end

	 return loc_max
end

-- main function
product_num = tonumber(io.read())

-- create & input profit matrix
profit_matrix = {}
tmp_profit_matrix = {}
profit_output = {}
for i = 1, product_num do
	profit_matrix[i] = {}
	tmp_profit_matrix[i] = {}
end
for i = 1, product_num do
	profit_str = io.read()
	-- construct profit matrix
	profit_matrix[i] = string.split(profit_str, " ")
end

tmp_profit_matrix = clone(profit_matrix)


-- calc max profit
ret = recursion_calc(tmp_profit_matrix, product_num, math.floor(product_num/2), profit_output, math.floor(product_num/2))
print("ret"..ret)
--[[
max_profit = 0
tmp_max_profit = 0
cnt = 0
tmp_i = 0
tmp_j = 0

--for sort_i = 1, (product_num * product_num - product_num)/2 do
for sort_i = 2, product_num - 1 do
	for sort_j = 1, sort_i - 1 do
		if tonumber(profit_matrix[sort_i][sort_j]) > 0 then
				tmp_i = sort_i
				tmp_j = sort_j
				max = tonumber(profit_matrix[sort_i][sort_j])
		end
	end
end
while cnt < math.floor(product_num/2) - 1 do
	max = 0
	for i = 2, product_num - 1 do
		for j = 1, i - 1 do
			if tonumber(profit_matrix[i][j]) > 0 then
				tmp_i = i
				tmp_j = j
				max = tonumber(profit_matrix[i][j])
			end
		end
	end
	for i = 1, product_num do
		for j = 1, i do
			if (i == tmp_i) || (j == tmp_i) || (i == tmp_j) || (j == tmp_j) then
				profit_matrix[tmp_i][tmp_j] = 0
			end
		end
	end
	cnt = cnt + 1
	tmp_max_profit = tmp_max_profit + max
	if (tmp_max_profit > max_profit) then
		max_profit = tmp_max_profit
	end
end

print(max_profit)]]--
