lua
local f, x, y = CreateFrame("Button", "CoordinateDisplay", UIParent, "UIGoldBorderButtonTemplate")
f:SetPoint("TOP", 0, 0)
f:SetWidth(80)

f:SetScript("OnUpdate", function(s, e)
    x, y = GetPlayerMapPosition("player")
    f:SetText(format("(%.1f,%.1f)", x * 100, y * 100))
end)