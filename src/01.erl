-module(aoc).
-export([main/1]).

-define(HUGE, 9999).

solve_1(Numbers) ->
    solve_1(Numbers, ?HUGE, 0).

solve_1([N|Rest], Previous, Result) ->
    NextResult = Result + case (N > Previous) of true -> 1; false -> 0 end,
    case Rest of
        [] -> NextResult;
        _ -> solve_1(Rest, N, NextResult)
    end.

main([Filename]) ->
    Numbers = get_parsed_lines(Filename, fun erlang:list_to_integer/1),
    io:fwrite("~w~n", [solve_1(Numbers)]).

%%
% IO Functions

get_parsed_lines(FileName, ParseFn) ->
    {ok, Device} = file:open(FileName, [read]),
    try
        parse_all_lines(Device, ParseFn)
    after
        file:close(Device)
    end.

parse_all_lines(Device, ParseFn) ->
    case io:get_line(Device, []) of
        eof  -> [];
        Line -> [ParseFn(string:trim(Line)) | parse_all_lines(Device, ParseFn)]
    end.
