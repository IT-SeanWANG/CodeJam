#!/usr/bin/lua

--[[
	write by Sean WANG
	environment: Windows 7 Lua5.1.5
	2017/04/19
]]--


-- split input string to table
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


-- **main function
blind_num = io.read()
--print(blind_num)

position_str = io.read()
--print(position_str)

-- define position table
blind_pos = string.split(position_str, " ")
sick_pos = blind_pos[1]

--[[
table.sort(blind_pos)
for key, value in ipairs(blind_pos)
do
	print(value)
end
]]--

sick_num = 1
flag_p = false
flag_n = false
if (tonumber(sick_pos) > 0) then
	for j = 2, blind_num do
		if tonumber(blind_pos[j]) < 0 and math.abs(tonumber(blind_pos[j])) > tonumber(sick_pos) then
			flag_p = true
			break
		end
	end
else
	for k = 2, blind_num do
		-- eg: -3 2 -10
		if tonumber(blind_pos[k]) > 0 and math.abs(tonumber(sick_pos)) > tonumber(blind_pos[k]) then
			flag_n = true
			break
		end
	end
end

for i = 1, blind_num do
	if (tonumber(sick_pos) > 0) then
		-- eg: 3 -4
		if tonumber(blind_pos[i]) < 0 and math.abs(tonumber(blind_pos[i])) > tonumber(sick_pos) then
			sick_num = sick_num + 1
		-- eg: 3 2 -10
		elseif flag_p and tonumber(blind_pos[i]) > 0 and tonumber(blind_pos[i]) < tonumber(sick_pos) then
				sick_num = sick_num + 1
		end
	else
		-- eg: -3 1
		if tonumber(blind_pos[i]) > 0 and math.abs(tonumber(sick_pos)) > tonumber(blind_pos[i]) then
			sick_num = sick_num + 1
		-- eg: -5 2 -10
		elseif  flag_n and tonumber(blind_pos[i]) < 0 and math.abs(tonumber(blind_pos[i])) > math.abs(tonumber(sick_pos)) then
			sick_num = sick_num + 1
		end
	end
end
print(sick_num)

