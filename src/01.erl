-module(aoc).
-export([main/1]).
-include("common/common.hrl").

-define(HUGE, 9999).

solve_1(Numbers) ->
    solve_1(Numbers, ?HUGE, 0).

solve_1([N|Rest], Previous, Result) ->
    NextResult = Result + case (N > Previous) of true -> 1; false -> 0 end,
    case Rest of
        [] -> NextResult;
        _ -> solve_1(Rest, N, NextResult)
    end.

solve_2(Numbers) ->
    solve_2(Numbers, ?HUGE, ?HUGE, ?HUGE, 0).

solve_2([N|Rest], P1, P2, P3, Result) ->
    NextResult = Result + case (N+P1+P2 > P1+P2+P3) of true -> 1; false -> 0 end,
    case Rest of
        [] -> NextResult;
        _ -> solve_2(Rest, N, P1, P2, NextResult)
    end.

main([Filename]) ->
    Numbers = get_parsed_lines(Filename, fun erlang:list_to_integer/1),
    io:fwrite("~w~n", [solve_1(Numbers)]),
    io:fwrite("~w~n", [solve_2(Numbers)]).
