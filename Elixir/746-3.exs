# Min Cost Climbing Stairs
# Medium

defmodule Solution do
    @spec min_cost_climbing_stairs(cost :: [integer]) :: integer
    def min_cost_climbing_stairs([h1, h2, h3 | tl]) do
        min_cost_climbing_stairs([h2, min(h1, h2) + h3 | tl])
    end
    def min_cost_climbing_stairs([h1, h2]), do: min(h1, h2)
end
