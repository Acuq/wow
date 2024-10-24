local f = CreateFrame("Frame", "CoordinateDisplay", UIParent)

f:SetWidth(120)
f:SetHeight(40)
f:SetPoint("TOP", UIParent, "TOP", 0, -5)

local text = f:CreateFontString(nil, "OVERLAY", "GameFontNormal")
text:SetPoint("CENTER", f, "CENTER")
text:SetFont("Fonts\\FRIZQT__.TTF", 14, "OUTLINE")

f:SetBackdrop({
    bgFile = "Interface\\Tooltips\\UI-Tooltip-Background",
    tile = true,
    tileSize = 20,
    insets = { left = 25, right = 25, top = -5, bottom = -5 }
})

f:SetBackdropColor(0, 0, 0, 1)

f:SetScript("OnUpdate", function(s, e)
    local x, y = GetPlayerMapPosition("player")
    if x == 0 and y == 0 then
        text:SetText("Not on map")
    else
        text:SetText(format("%.2f\n\n%.2f", x * 100, y * 100))
    end
end)