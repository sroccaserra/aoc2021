-module(aoc).
-export([main/1]).
-include("common/common.hrl").

-define(HUGE, 9999).

solve_1(Numbers) ->
    solve_1(Numbers, ?HUGE, 0).

solve_1([], _, Result) ->
    Result;

solve_1([N | Rest], Previous, Result) ->
    case N > Previous of
        true -> solve_1(Rest, N, Result + 1);
        false -> solve_1(Rest, N, Result)
    end.

solve_2(Numbers) ->
    solve_2(Numbers, ?HUGE, ?HUGE, ?HUGE, 0).

solve_2([], _, _, _, Result) ->
    Result;

solve_2([N | Rest], P1, P2, P3, Result) ->
    case (N+P1+P2 > P1+P2+P3) of
        true -> solve_2(Rest, N, P1, P2, Result + 1);
        false -> solve_2(Rest, N, P1, P2, Result)
    end.

main([Filename]) ->
    Numbers = get_parsed_lines(Filename, fun erlang:list_to_integer/1),
    io:fwrite("~w~n", [solve_1(Numbers)]),
    io:fwrite("~w~n", [solve_2(Numbers)]).
