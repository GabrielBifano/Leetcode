# Maximum Twin Sum of a Linked List
# Medium

defmodule ListNode do
  @type t :: %__MODULE__{
    val: integer,
    next: ListNode.t() | nil
  }
  defstruct val: 0, next: nil
end


defmodule Solution do
  @spec pair_sum(head :: ListNode.t | nil) :: integer
  def pair_sum(head) do
    halve_it(head, head, [])
    |> maxsum(0)
  end

  defp halve_it(mid, nil, stack), do: {mid, stack}
  defp halve_it(mid, endpoint, stack) do
    halve_it(mid.next, endpoint.next.next, [mid.val | stack])
  end

  defp maxsum({mid, [x | stack]}, csum) do
    maxsum({mid.next, stack}, max(csum, mid.val + x))
  end
  defp maxsum(_, csum), do: csum
end
