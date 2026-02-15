-- columns.lua
function Para(el)
  -- Count how many images are in this paragraph
  local images = 0
  for _, inline in ipairs(el.content) do
    if inline.t == "Image" then
      images = images + 1
    end
  end

  -- If there is more than one image, we need to make them smaller to fit on one line
  if images > 1 then
    for _, inline in ipairs(el.content) do
      if inline.t == "Image" then
        inline.attributes['width'] = "45%"
      end
    end
  elseif images == 1 then
    -- If it's a single image, keep it at your preferred 80%
    for _, inline in ipairs(el.content) do
      if inline.t == "Image" then
        inline.attributes['width'] = "80%"
      end
    end
  end
  return el
end
