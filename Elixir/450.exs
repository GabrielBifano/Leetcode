defmodule TreeNode do
  @type t :: %__MODULE__{
    val: integer,
    left: TreeNode.t() | nil,
    right: TreeNode.t() | nil
  }
  defstruct val: 0, left: nil, right: nil
end

defmodule Solution do
  @spec delete_node(root :: TreeNode.t | nil, key :: integer) :: TreeNode.t | nil
  def delete_node(root, key) do

  end

  defp dfs(nil, _) do: nil
  defp dfs(node, key) do
    if node.val < key do
      dfs(node.left,  key)
    else
      dfs(node.right, key)
    end
    # dfs(node.left), node.val < key | dfs(node.right), node.val > key
  end
end
