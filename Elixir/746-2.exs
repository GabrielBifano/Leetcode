# Min Cost Climbing Stairs
# Medium

defmodule Solution do
    @spec min_cost_climbing_stairs(cost :: [integer]) :: integer
    def min_cost_climbing_stairs([h1, h2 | tl]) do
        total_cost(tl, [h2, h1])
    end

    defp total_cost([], [x1, x2]), do: min(x1, x2)
    defp total_cost(cost, [h1, h2 | t]) do
        last = min(h1, h2) + hd(cost)
        total = [last] ++ [h1]
        total_cost(tl(cost), total)
    end
end
